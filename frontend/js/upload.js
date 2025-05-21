const API_URL = 'http://127.0.0.1:8000';

document.getElementById('uploadForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const credorId = document.getElementById('credorId').value;
  const tipo = document.getElementById('tipoDocumento').value;
  const file = document.getElementById('file').files[0];

  const formData = new FormData();
  formData.append('tipo', tipo);
  formData.append('file', file);

  fetch(`${API_URL}/credores/${credorId}/documentos`, {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => alert(data.message || 'Documento enviado com sucesso!'))
  .catch(error => alert('Erro ao enviar: ' + error));
});

async function loadCredores() {
    const tbody = document.getElementById('credorId');
    tbody.innerHTML = '';
    const res = await fetch(API_URL + '/credores')
    .then(res => res.json())
    .then(credor => {
      console.log(credor)
        credor.data.forEach(c => {
        tbody.innerHTML += `
                <option value=${c.id}>${c.nome}</option>
            `;
        });
    })
    .catch(err => {
        console.error('Erro ao carregar credores:', err);
    });
}

loadCredores();
