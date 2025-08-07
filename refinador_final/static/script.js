document.getElementById("form-aprimorar").addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(e.target);

    fetch("/aprimorar", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const mensagem = document.getElementById("mensagem");
        const nivelSpan = document.getElementById("nivel-" + data.index);
        nivelSpan.textContent = data.nivel;

        if (data.resultado === "sucesso") {
            mensagem.innerHTML = "<span class='text-success'>Sucesso! Item aprimorado!</span>";
        } else {
            mensagem.innerHTML = "<span class='text-danger'>Falha! Item resetado para o nível 0.</span>";
        }

        const logList = document.getElementById("log-list");

        if (data.log && Array.isArray(data.log)) {
            logList.innerHTML = "";
            data.log.forEach(entry => {
                const li = document.createElement("li");
                li.textContent = entry;
                li.className = "list-group-item bg-dark text-light";
                logList.appendChild(li);
            });
        }
    });
});