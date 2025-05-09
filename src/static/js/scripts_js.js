document.getElementById('real-file-input').addEventListener('change', function(e) {
    const fileInput = e.target;
    const statusElement = document.getElementById('file-status');
    
    if (fileInput.files.length > 0) {
      const fileName = fileInput.files[0].name;
      statusElement.textContent = 'Изображение принято';
    } else {
      statusElement.textContent = 'Файл не выбран';
    }
  });


// file_name.js

document.addEventListener('DOMContentLoaded', () => {
    const realFileInput = document.getElementById('real-file-input');
    const fileStatus = document.getElementById('file-status');
    const form = document.querySelector('.form');
    const submitButton = form?.querySelector('button[type="submit"]');
    const textarea = document.querySelector('textarea.text-for-post'); // Измененный селектор

    const handleFormSubmit = async (event) => {
        event.preventDefault();

        try {
            // 1. Собираем FormData
            const formData = new FormData(form); // Автоматически соберет все поля формы

            // 2. Добавляем файл вручную (если есть)
            if (realFileInput.files[0]) {
                formData.append('image', realFileInput.files[0]);
            }

            // 3. Отладочный вывод (можно удалить после тестирования)
            for (let [key, value] of formData.entries()) {
                console.log(key, value);
            }

            // 4. Отправка на сервер
            const response = await fetch('/api/posts/', {
                method: 'POST',
                body: formData // Не нужно устанавливать Content-Type - браузер сделает это сам
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || 'Ошибка сервера');
            }

            const result = await response.json();
            window.location.href = `/posts/${result.id}`;
        } catch (error) {
            console.error('Ошибка:', error);
            alert(error.message);
        }
    };

    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});