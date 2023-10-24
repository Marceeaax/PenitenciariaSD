function buscarRecluso() {
    const reclusoID = document.getElementById('reclusoID').value;
    fetch(`http://127.0.0.1:5000/Reclusos/${reclusoID}`)
        .then(response => response.json())
        .then(data => {
            const detalles = JSON.stringify(data, null, 2);  // Formatea el JSON con 2 espacios de indentación.
            document.getElementById('reclusoDetalles').textContent = detalles;
        })
        .catch(error => {
            console.error("Error al buscar el recluso:", error);
            alert("Error al buscar el recluso. Por favor, intenta nuevamente.");
        });
}
