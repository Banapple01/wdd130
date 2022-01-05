const links = [
    {
        label: "Week 1 notes",
        url: "week1/index.html"
    }
]

const ol = document.querySelector('#weekly')
links.forEach(e => {
    console.log(e)
    let lab = document.createElement('li')
    lab.textContent = e['label'];
    let ur = document.createElement('a')
    ur.setAttribute('src', e['url'])
    ol.appendChild(lab)
    ol.appendChild(ur)
});