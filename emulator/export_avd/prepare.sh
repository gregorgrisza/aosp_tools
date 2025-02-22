#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cp -vf $SCRIPT_DIR/v-sys-img2-1.xml $SCRIPT_DIR/../../../../../out/target/product/mycar_x86/
