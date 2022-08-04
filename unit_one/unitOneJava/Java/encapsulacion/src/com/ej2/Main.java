package com.ej2;

public class Main {
    public static void main(String[] args){
    Cliente cliente = new Cliente();
    cliente.age = 23;
    cliente.name = "Francisco";
    cliente.telephone = 1604830;
    cliente.credit = 20000;
        System.out.println("El cliente " + cliente.name + " de " + cliente.age + " con el numero de telefono: " + cliente.telephone + " posee un credito de " + cliente.credit);
    }
}

class Persona {
    String name;
    int age;
    int telephone;
}

class Cliente extends Persona {
    int credit;
}
