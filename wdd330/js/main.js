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
    let ur = document.createElement('a')
    ur.setAttribute('src', e['url'])
    ur.textContent = e['label']
    lab.appendChild(ur)
    ol.appendChild(lab)
});