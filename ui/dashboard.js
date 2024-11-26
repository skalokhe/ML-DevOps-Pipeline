fetch('/metrics')
  .then(response => response.json())
  .then(data => {
    document.getElementById('pipeline-status').innerText = `Pipeline Status: ${data.status}`;
  });
