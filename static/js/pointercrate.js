fetch("/api/demons/pointercrate/")
    .then(resp => resp.json())
    .then(data => {
        for (let i = 0; i < data.length; i++) {            
            document.getElementById("demons").innerHTML += `<div class="card">
            <div class="card-body">
                <img class="link" src=${data[i].thumbnail} alt="${data[i].name}" onclick="location.href = '${data[i].video}'">
                <br>
                <br>
                <h1>#${data[i].position} - ${data[i].name}</h1>
                <p>${data[i].verifier.name}</p>
            </div>
        </div> 
        <br>`
    }
})