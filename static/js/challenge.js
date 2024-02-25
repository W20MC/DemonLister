fetch("/api/demons/challenge/")
    .then(resp => resp.json())
    .then(data => {
        for (let i = 0; i < data.length; i++) {
            const video_id = new URL(data[i].video).searchParams.get("v")
            const thumb = `https://img.youtube.com/vi/${video_id}/mqdefault.jpg`
            
            document.getElementById("demons").innerHTML += `<div class="card">
            <div class="card-body">
                <img class="link" src=${thumb} alt="${data[i].name}" onclick="location.href = '${data[i].video}'">
                <br>
                <br>
                <h1>#${data[i].position} - ${data[i].name}</h1>
                <p>${data[i].verifier.name}</p>
            </div>
        </div> 
        <br>`
    }
})