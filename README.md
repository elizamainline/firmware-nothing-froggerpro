# Nothing Phone (4a) Pro firmware

Firmware for the Nothing Phone (4a) Pro (FroggerPro, A069P, Qualcomm SM7750).
The files were extracted from a European retail device running
`Nothing/FroggerProEEA/FroggerPro:16/BQ2A.250913.001-BP2A.250605.031.A3/2607231820:user/release-keys`.

The `lib/firmware` tree contains firmware loaded by Linux drivers. Qualcomm
PIL images were combined from the stock `.mdt` and `.bXX` files using
[`pil-squasher`](https://github.com/andersson/pil-squasher). The
`usr/share/qcom` tree contains the stock audio calibration, DSP libraries and
sensor configuration used by Qualcomm userspace.

Personal calibration and identifiers from `/mnt/vendor/persist` are not
included. The radio bootloader partition images are also outside this runtime
firmware collection.

The files are proprietary and retain their owners' licenses. No license to
redistribute or modify them is granted by this repository.
