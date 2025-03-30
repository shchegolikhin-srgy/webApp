let content = JSON.parse(localStorage.getItem('content')) || {
    'post1': 'Lorem Ipsum...',
    'post2': 'Contrary to popular belief...'
};
function addContent() {
    const title = document.getElementById('title').value;
    const text = document.getElementById('content').value;
    
    if (title && text) {
        
        content[title] = text;
        localStorage.setItem('content', JSON.stringify(content));
        console.log(content[title])
        document.getElementById('title').value = '';
        document.getElementById('content').value = '';
        
        document.getElementById('message').textContent = 'Пост успешно добавлен!';
        document.getElementById('message').style.color = 'green';
        
    } else {
        document.getElementById('message').textContent = 'Заполните все поля!';
        document.getElementById('message').style.color = 'red';
    }
}
function addArticles() {
    let count =1
    for (let key in content) {
        const article = document.createElement('article');
        article.innerHTML = `<h2>${key}</h2><p>${content[key]}</p>`;
        mainElement.appendChild(article);
    }
}

function addRecomendation() {
    for (let key in content) {
        const newElement = document.createElement('article');
        const mainElement = document.querySelector('main'); 
        newElement.innerHTML = '<article><a href="articles"><h2>' + key + '</h2></a></article>';
        mainElement.appendChild(newElement);
    }
}




function getCurrentPage() {
    const currentPage = document.body.getAttribute('data-page');
    if (currentPage == "home") { addRecomendation(); }
    if (currentPage == "articles") { addArticles(); }
}

getCurrentPage();   