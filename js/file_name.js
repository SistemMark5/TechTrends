document.getElementById('real-file-input').addEventListener('change', function(e) {
    const fileInput = e.target;
    const statusElement = document.getElementById('file-status');
    
    if (fileInput.files.length > 0) {
      const fileName = fileInput.files[0].name;
      statusElement.textContent = `Изображение принято`;
    } else {
      statusElement.textContent = 'Файл не выбран';
    }
  });