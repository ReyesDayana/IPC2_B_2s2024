const objeto = { nombre: "Ana", edad: undefined, casado: false, decirHola: () => "Hola" };
const cadenaJSON = JSON.stringify(objeto);

console.log(cadenaJSON);
// Resultado: {"nombre":"Ana","casado":false}