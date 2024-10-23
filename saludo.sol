// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

contract Saludo {

    string saludo = "Saludo desde REMIX";

    function leerSaludo() public view returns (string memory) {
        return saludo;
    }

    function guardarSaludo(string memory _nuevoSaludo) public {
        saludo = _nuevoSaludo;
    }
    
}