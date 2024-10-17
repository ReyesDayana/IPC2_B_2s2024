try {
    const malJSON = "{'nombre': 'Ana'}"; 
    JSON.parse(malJSON);
} catch (error) {
    console.error("Error al parsear JSON: ", error.message);
}