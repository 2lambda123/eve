# syntax=docker/dockerfile-upstream:1.5.0-rc2-labs
FROM lfedge/eve-alpine:9fb9b9cbf7d90066a70e4704d04a6fe248ff52bb as build-base
RUN mkdir /bsp

FROM build-base AS build-amd64
FROM build-base AS build-riscv64
FROM build-base AS build-arm64
ENV BUILD_PKGS bash binutils-dev build-base bc bison flex openssl-dev util-linux-dev swig gnutls-dev perl python3 python3-dev py3-setuptools py3-pycryptodome py3-elftools
RUN eve-alpine-deploy.sh

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

ENV UBOOT_TARGETS "imx8mq_evk imx8mp_pollux imx8mp_epc_r3720"
ENV ATF_TARGETS "imx8mq_evk imx8mp_pollux imx8mp_epc_r3720"

RUN mkdir /uboot-firmwares

COPY patches /tmp/patches

# ATF
WORKDIR /imx-atf

# imx8mq_evk: last commit from imx_5.4.70_2.3.0 branch
ENV ATF_COMMIT_imx8mq_evk 15e8ff164a8becfddb76cba2c68eeeae684cb398
ENV ATF_imx8mq_evk "imx8mq"
ENV ATF_SRC_imx8mq_evk "imx8mq_evk"
ENV ATF_UART_imx8mq_evk "0x30860000"

# Phytec phyBOARD-pollux
# Revision used by phytec's yocto bsp: lf-5.10.72-2.2.0
ENV ATF_COMMIT_imx8mp_pollux 5782363f92a2fdf926784449270433cf3ddf44bd
ENV ATF_imx8mp_pollux "imx8mp"
ENV ATF_SRC_imx8mp_pollux "pollux"
ENV ATF_UART_imx8mp_pollux "0x30860000"

# Advantech EPC-R3720
ENV ATF_COMMIT_imx8mp_epc_r3720 5782363f92a2fdf926784449270433cf3ddf44bd
ENV ATF_imx8mp_epc_r3720 "imx8mp"
ENV ATF_SRC_imx8mp_epc_r3720 "epc-r3720"
ENV ATF_UART_imx8mp_epc_r3720 "0x30880000"

# Repositories
ADD https://github.com/nxp-imx/imx-atf.git#${ATF_COMMIT_imx8mq_evk} ${ATF_SRC_imx8mq_evk}
ADD https://github.com/nxp-imx/imx-atf.git#${ATF_COMMIT_imx8mp_pollux} ${ATF_SRC_imx8mp_pollux}
ADD https://github.com/nxp-imx/imx-atf.git#${ATF_COMMIT_imx8mp_epc_r3720} ${ATF_SRC_imx8mp_epc_r3720}
# hadolint ignore=DL3003,SC2086
RUN for t in ${ATF_TARGETS}; do \
        target=$(eval echo \$ATF_${t}) ;\
        repo=$(eval echo \$ATF_SRC_${t}) ;\
        uartbase=$(eval echo \$ATF_UART_${t}) ;\
        patchdir=$(eval echo /tmp/patches/atf-${t}) ;\
        (cd ${repo} ;\
         [ -d "$patchdir" ] && for p in "${patchdir}"/*.patch ; do patch -p1 < "$p"; done ;\
         make clean && \
         make -j "$(getconf _NPROCESSORS_ONLN)" \
            IMX_BOOT_UART_BASE="${uartbase}" \
            PLAT=${target} \
            bl31 ;\
         mv build/${target}/release/bl31.bin /uboot-firmwares/${t}-bl31.bin) ;\
    done

# IMX firmware
WORKDIR /tmp
ENV FIRMWARE_VER=8.18
ADD https://www.nxp.com/lgfiles/NMG/MAD/YOCTO/firmware-imx-${FIRMWARE_VER}.bin firmware-imx-${FIRMWARE_VER}.bin
RUN chmod 777 firmware-imx-${FIRMWARE_VER}.bin && \
        echo "n" | ./firmware-imx-8.18.bin | head -n -1 > /bsp/NXP-EULA-LICENSE.txt || true && \
        ./firmware-imx-${FIRMWARE_VER}.bin --auto-accept && \
        rm firmware-imx-${FIRMWARE_VER}.bin && \
        mv firmware-imx-${FIRMWARE_VER}/firmware /firmware

# Copy all the necessary firmware for u-boot
ENV DDR_FIRMWARE "ddr/synopsys/lpddr4_pmu_train_1d_imem.bin \
 ddr/synopsys/lpddr4_pmu_train_1d_dmem.bin \
 ddr/synopsys/lpddr4_pmu_train_2d_imem.bin \
 ddr/synopsys/lpddr4_pmu_train_2d_dmem.bin \
 ddr/synopsys/lpddr4_pmu_train_1d_imem_202006.bin \
 ddr/synopsys/lpddr4_pmu_train_1d_dmem_202006.bin \
 ddr/synopsys/lpddr4_pmu_train_2d_imem_202006.bin \
 ddr/synopsys/lpddr4_pmu_train_2d_dmem_202006.bin \
"
ENV VIDEO_FIRMWARE "hdmi/cadence/signed_hdmi_imx8m.bin"
RUN for firmware_file in ${DDR_FIRMWARE} ${VIDEO_FIRMWARE}; do \
        cp /firmware/${firmware_file} /uboot-firmwares ;\
    done


ENV UBOOT_VERSION lf_v2022.04
ENV UBOOT_COMMIT 181859317bfafef1da79c59a4498650168ad9df6
WORKDIR /u-boot-imx
ADD https://github.com/nxp-imx/uboot-imx.git#${UBOOT_COMMIT} .
RUN mv /uboot-firmwares/* .

RUN for p in /tmp/patches/uboot-patches-"${UBOOT_VERSION}"/*.patch ; do patch -p1 < "$p" || exit 1 ; done

# u-boot target and files for imx8mq_evk board
ENV UBOOT_FILES_imx8mq_evk "flash.bin"
ENV UBOOT_CONFIG_imx8mq_evk "imx8mq_evk"
ENV FLASH_OFFSET_imx8mq_evk "33"

# u-boot target and files for imx8mp_pollux
ENV UBOOT_FILES_imx8mp_pollux "flash.bin"
ENV UBOOT_CONFIG_imx8mp_pollux "phycore-imx8mp"
ENV UBOOT_DTB_imx8mp_pollux "arch/arm/dts/imx8mp-phyboard-pollux-rdk.dtb"
ENV FLASH_OFFSET_imx8mp_pollux "32"

# u-boot target and files for imx8mp_epc_r3720
ENV UBOOT_FILES_imx8mp_epc_r3720 "flash.bin"
ENV UBOOT_CONFIG_imx8mp_epc_r3720 "imx8mp_rsb3720a1_6G"
ENV UBOOT_DTB_imx8mp_epc_r3720 "arch/arm/dts/imx8mp-rsb3720-a1.dtb"
ENV FLASH_OFFSET_imx8mp_epc_r3720 "32"

# hadolint ignore=SC2086
RUN for target in ${UBOOT_TARGETS}; do \
        make clean && rm -rf bl31.bin && \
        cp "${target}"-bl31.bin bl31.bin && \
        make "$(eval echo \$UBOOT_CONFIG_${target})"_defconfig && \
        make -j "$(getconf _NPROCESSORS_ONLN)" ;\
        for file in "$(eval echo \$UBOOT_FILES_"${target}")"; do \
            cp $file /bsp/${target}-${file} ;\
        done;\
        offset=$(eval echo \$FLASH_OFFSET_${target}) ;\
        echo "# Bootloader offset" > /bsp/${target}-flash.conf ;\
        echo "offset=${offset}" >> /bsp/${target}-flash.conf ;\
        udtb=$(eval echo \$UBOOT_DTB_"${target}") ;\
        [ -f "$udtb" ] && cp $udtb /bsp/ ;\
    done

# hadolint ignore=DL3006
FROM build-${TARGETARCH} AS bsp-imx-build

FROM scratch
ENTRYPOINT []
CMD []
COPY --from=bsp-imx-build /bsp /bsp-imx
