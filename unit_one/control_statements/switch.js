/*Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.*/
let estacion = "papafrita";
switch (estacion) {
  case "invierno":
    console.log("la estacion es invierno");
    break;
  case "verano":
    console.log("la estacion es verano");
    break;
  case "primavera":
    console.log("la estacion es primavera");
    break;
  case "otoño":
    console.log("la estacion es otoño");
  default:
    console.log("el valor ingresado no es una estacion");
    break;
}
