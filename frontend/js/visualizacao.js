const API_URL = 'http://127.0.0.1:8000';

async function loadArquivosDocumentos() {
    const tbody = document.getElementById('list-documentos');
    tbody.innerHTML = '';
    const res = await fetch(API_URL + '/credores')
    .then(res => res.json())
    .then(credor => {
        credor.data.forEach(c => {
            c.documentos.forEach(d => {
                tbody.innerHTML += `
                    <div class="col">
                        <div class="card h-100">
                            <div class="card-body">
                                <h5 class="card-title">${d.arquivo_url}</h5>
                                <p class="card-text">Credor: ${c.nome}</p>
                                <p class="card-text">Enviado em: ${d.enviado_em}</p>
                                <a href="#" class="btn btn-outline-primary btn-sm">Visualizar</a>
                                <a href="#" class="btn btn-outline-secondary btn-sm">Download</a>
                            </div>
                        </div>
                    </div>
                `; 
            })      
        });
    })
    .catch(err => {
        console.error('Erro ao carregar credores:', err);
    });
}

loadArquivosDocumentos();