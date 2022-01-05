const links = [
    {
        label: "Week1 notes",
        url: "week1/index.html"
    }
]

const ol = document.querySelector('#weekly')
links.forEach(e => {
    console.log(e)
    let lab = document.createElement('li').textContent = e['label'];
    let ur = document.createElement('li').textContent = e['url'];
    ol.appendChild(lab)
    ol.appendChild(ur)
});