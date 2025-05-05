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


// file_name.js

document.addEventListener('DOMContentLoaded', () => {
    // Элементы DOM
    const realFileInput = document.getElementById('real-file-input');
    const fileStatus = document.getElementById('file-status');
    const form = document.querySelector('.form');
    const submitButton = form?.querySelector('button[type="submit"]');
    const textarea = document.querySelector('.text-for-post');

    // Обработчики событий
    const setupEventListeners = () => {
        if (realFileInput && fileStatus) {
            realFileInput.addEventListener('change', handleFileSelect);
        }

        if (form) {
            form.addEventListener('submit', handleFormSubmit);
        }
    };

    // Обработка выбора файла
    const handleFileSelect = (event) => {
        const file = event.target.files[0];
        fileStatus.textContent = file ? file.name : 'Изображение не выбрано';
    };

    // Валидация формы
    const validateForm = (formData) => {
        if (!formData.get('title')?.trim()) {
            throw new Error('Заголовок поста обязателен');
        }

        if (!formData.get('text')?.trim()) {
            throw new Error('Текст поста обязателен');
        }

        const file = realFileInput.files[0];
        if (file) {
            const validTypes = ['image/jpeg', 'image/png', 'image/gif'];
            if (!validTypes.includes(file.type)) {
                throw new Error('Допустимы только изображения JPEG, PNG или GIF');
            }

            if (file.size > 10 * 1024 * 1024) {
                throw new Error('Размер файла не должен превышать 10MB');
            }
        }
    };

    // Отправка данных на сервер
    const sendPostData = async (formData) => {
        try {
            const response = await fetch('/api/posts/', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Ошибка сервера');
            }

            return await response.json();
        } catch (error) {
            console.error('Ошибка при отправке:', error);
            throw error;
        }
    };

    // Обработка отправки формы
    const handleFormSubmit = async (event) => {
        event.preventDefault();

        if (!submitButton) return;

        try {
            // Подготовка данных формы
            const formData = new FormData();
            formData.append('title', document.getElementById('post-title').value);
            formData.append('text', textarea.value);
            formData.append('from_title', document.getElementById('source').value);
            formData.append('title_image', document.getElementById('image-source').value);

            if (realFileInput.files[0]) {
                formData.append('image', fileInput.files[0]);  // Важно: имя 'image'
            }

            // Валидация
            validateForm(formData);

            // UI - показать загрузку
            submitButton.disabled = true;
            submitButton.textContent = 'Отправка...';

            // Отправка данных
            const result = await sendPostData(formData);

            // Успешная отправка
            alert('Пост успешно создан!');
            window.location.href = `/posts/${result.id}`;

        } catch (error) {
            // Обработка ошибок
            alert(`Ошибка: ${error.message}`);
            console.error('Ошибка создания поста:', error);
        } finally {
            // UI - восстановить состояние кнопки
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.textContent = 'Опубликовать';
            }
        }
    };

    // Инициализация
    setupEventListeners();
});