let name = "Daiana";

let surname = "Terranova";

let student = name.concat(
  ` ${surname}`
); /* otra opcion podria ser name.concat("", surname) */

let estudianteMayus = student.toUpperCase();

let estudianteMinus = student.toLowerCase();

let charNumb = student.length;

let firstCharName = name.charAt(0);

let lastCharName = surname.charAt(surname.length - 1);

let withOutSpace = student.replace(/ /g, "");

let hasName = student.includes(name);
