/**
 *Submitted for verification at Etherscan.io on 2023-10-11
*/

// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.13 <0.9.0;

contract HashesAreSafe {

    constructor() {
    }

    function checkFlag(string memory _input) pure public returns (bool) {

        if (keccak256(abi.encodePacked(_input)) == 0xc6529caaeee374d860f327f47f18a6585df16f8d87581d71bccbe16af79e86e1)
        {
            return true;
        } else {
            return false;
        }
    }
}