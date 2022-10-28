// Copyright (c) 2022 Zededa, Inc.
// SPDX-License-Identifier: Apache-2.0

package volumehandlers

import (
	zconfig "github.com/lf-edge/eve/api/go/config"
	"github.com/lf-edge/eve/pkg/pillar/base"
	"github.com/lf-edge/eve/pkg/pillar/cas"
	"github.com/lf-edge/eve/pkg/pillar/types"
	"github.com/lf-edge/eve/pkg/pillar/vault"
)

// VolumeHandler implements processing of different volumes types
type VolumeHandler interface {
	// PrepareVolume handles preparation process
	PrepareVolume() error
	// HandlePrepared handles preparation done
	HandlePrepared() (bool, error)
	// CreateVolume handles creation process
	CreateVolume() (string, error)
	// HandleCreated handles creation done
	HandleCreated() (bool, error)
	// DestroyVolume handles destroy process
	DestroyVolume() (string, error)
	// Populate fills VolumeStatus with the information from previously created volume
	Populate() (bool, error)
	// GetVolumeDetails returns ActualSize, VirtualSize, Format, DirtyFlag and possible error
	GetVolumeDetails() (uint64, uint64, string, bool, error)
	// UsageFromStatus returns calculated usage of volume
	// with current options of VolumeStatus
	// to be used in storage usage calculation
	UsageFromStatus() uint64
}

// VolumeMgr is an interface to obtain information required for volume processing
type VolumeMgr interface {
	LookupVolumeConfig(key string) *types.VolumeConfig
	LookupVolumeStatus(key string) *types.VolumeStatus
	LookupContentTreeStatus(key string) *types.ContentTreeStatus
	LookupBlobStatus(blobSha string) *types.BlobStatus
	LookupZVolStatusByDataset(dataset string) *types.ZVolStatus
	GetCapabilities() *types.Capabilities
	GetCasClient() cas.CAS
}

// useZVolDisk returns true if we should use zvol for the provided VolumeStatus
func useZVolDisk(status *types.VolumeStatus) bool {
	if status.IsContainer() {
		return false
	}
	if status.ContentFormat == zconfig.Format_ISO {
		return false
	}
	return vault.ReadPersistType() == types.PersistZFS
}

func useVhost(log *base.LogObject, volumeManager VolumeMgr) bool {
	caps := volumeManager.GetCapabilities()
	if caps == nil {
		log.Error("no capabilities info")
		return false
	}
	return caps.UseVHost
}

// GetVolumeHandler returns handler based on provided status
func GetVolumeHandler(log *base.LogObject, volumeManager VolumeMgr, status *types.VolumeStatus) VolumeHandler {
	common := commonVolumeHandler{volumeManager: volumeManager, status: status, log: log}
	if status.IsContainer() {
		return &volumeHandlerContainer{common}
	}
	if useZVolDisk(status) {
		return &volumeHandlerZVol{commonVolumeHandler: common, useVHost: useVhost(log, volumeManager)}
	}
	return &volumeHandlerFile{common}
}

func updateVolumeSizes(log *base.LogObject, handler VolumeHandler, status *types.VolumeStatus) {
	if status.MaxVolSize == 0 {
		_, maxVolSize, _, _, err := handler.GetVolumeDetails()
		if err != nil {
			log.Error(err)
		} else if maxVolSize != status.MaxVolSize {
			log.Functionf("updateVolumeSizes: MaxVolSize update from  %d to %d for %s",
				status.MaxVolSize, maxVolSize,
				status.FileLocation)
			status.MaxVolSize = maxVolSize
		}
	}
}