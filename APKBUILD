# Reference: <https://postmarketos.org/devicepkg>
maintainer="Oleksii Onchul <oleksiionchul@gmail.com>"
pkgname=firmware-nothing-froggerpro
pkgver=20260723
pkgrel=0
pkgdesc="Firmware for the Nothing Phone (4a) Pro"
url="https://github.com/elizamainline/firmware-nothing-froggerpro"
arch="aarch64"
license="proprietary"
options="!check !strip !archcheck !tracedeps pmb:cross-native"
subpackages="
	$pkgname-adreno
	$pkgname-adsp
	$pkgname-audio
	$pkgname-bluetooth
	$pkgname-cdsp
	$pkgname-dsp
	$pkgname-ipa
	$pkgname-modem
	$pkgname-sensors
	$pkgname-vpu
	$pkgname-wpss
"
_commit="0c71e8293d53bd50674c28001a79e4c49d334cf8"
_fwdir="lib/firmware/qcom/sm7750/nothing/froggerpro"
_sharedir="usr/share/qcom/sm7750/Nothing/FroggerPro"
source="$pkgname-$_commit.tar.gz::$url/archive/$_commit.tar.gz"
builddir="$srcdir/$pkgname-$_commit"

package() {
	# All files belong to the firmware subpackages.
	mkdir -p "$pkgdir"
}

install_files() {
	local file dest
	for file in "$@"; do
		case "$file" in
			usr/*) dest="$subpkgdir/$file" ;;
			*) dest="$subpkgdir/usr/$file" ;;
		esac
		install -Dm644 "$builddir/$file" "$dest"
	done
}

install_tree() {
	local dest
	case "$1" in
		usr/*) dest="$subpkgdir/$1" ;;
		*) dest="$subpkgdir/usr/$1" ;;
	esac
	mkdir -p "$(dirname "$dest")"
	cp -a "$builddir/$1" "$dest"
	find "$dest" -type f -exec chmod 0644 {} +
}

adreno() {
	pkgdesc="Adreno firmware for the Nothing Phone (4a) Pro"
	install_files \
		"$_fwdir/gen70900_aqe.fw" \
		"$_fwdir/gen70900_sqe.fw" \
		"$_fwdir/gen70900_zap.mbn" \
		"$_fwdir/gmu_gen70900.bin"
}

adsp() {
	pkgdesc="ADSP firmware for the Nothing Phone (4a) Pro"
	install_files \
		"$_fwdir/adsp.mbn" \
		"$_fwdir/adsp_dtb.mbn" \
		"$_fwdir/adspr.jsn" \
		"$_fwdir/adsps.jsn" \
		"$_fwdir/adspua.jsn" \
		"$_fwdir/battmgr.jsn"
}

audio() {
	pkgdesc="Audio calibration data for the Nothing Phone (4a) Pro"
	install_tree "$_sharedir/acdb"
}

bluetooth() {
	pkgdesc="Bluetooth firmware for the Nothing Phone (4a) Pro"
	install_files \
		"lib/firmware/qca/msbtfw12.mbn" \
		"lib/firmware/qca/msnv12.bin"
}

cdsp() {
	pkgdesc="CDSP firmware for the Nothing Phone (4a) Pro"
	install_files \
		"$_fwdir/cdsp.mbn" \
		"$_fwdir/cdsp_dtb.mbn" \
		"$_fwdir/cdspr.jsn"
}

dsp() {
	pkgdesc="DSP libraries for the Nothing Phone (4a) Pro"
	install_tree "$_sharedir/dsp"
}

ipa() {
	pkgdesc="IPA firmware for the Nothing Phone (4a) Pro"
	install_files "$_fwdir/ipa_fws.mbn"
}

modem() {
	pkgdesc="Modem firmware for the Nothing Phone (4a) Pro"
	install_files \
		"$_fwdir/modem.mbn" \
		"$_fwdir/modem_dtb.mbn" \
		"$_fwdir/modemr.jsn"
	install_tree "$_fwdir/modem_pr"
}

sensors() {
	pkgdesc="Sensor configuration for the Nothing Phone (4a) Pro"
	install_tree "$_sharedir/sensors"
}

vpu() {
	pkgdesc="VPU firmware for the Nothing Phone (4a) Pro"
	local file
	for file in "$builddir/$_fwdir"/vpu*.mbn; do
		install_files "$_fwdir/${file##*/}"
	done
}

wpss() {
	pkgdesc="QCA6750 WPSS and WLAN firmware for the Nothing Phone (4a) Pro"
	install_tree "lib/firmware/qca6750"
}

sha512sums="
SKIP  firmware-nothing-froggerpro-0c71e8293d53bd50674c28001a79e4c49d334cf8.tar.gz
"
