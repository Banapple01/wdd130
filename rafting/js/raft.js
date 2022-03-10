var slidePosition = 0;
SlideShow();

function SlideShow() {
    var i;
    var slides = document.getElementsByClassName("Containers");
    for (i = 0; i < slides.length; i++) {
        // console.log(slides[i].children[0].classList.contains("ptagFadingIn"))
        if(slides[i].children[0].classList.contains("ptagFadingIn")){
            slides[i].children[0].classList.remove("ptagFadingIn")
            slides[i].children[0].classList.add("ptagFadingOut");
            setTimeout((slide)=>{
                slide.children[0].setAttribute("hidden", true)
                next()
            }, 400, slides[i])
        }
    }
    function next(){
        slidePosition++;
        var slides = document.getElementsByClassName("Containers");
        if (slidePosition > slides.length) {slidePosition = 1}
        slides[slidePosition-1].children[0].classList.remove("ptagFadingOut")
        slides[slidePosition-1].children[0].setAttribute("hidden", false)
        slides[slidePosition-1].children[0].removeAttribute("hidden", false)
        slides[slidePosition-1].children[0].classList.add("ptagFadingIn");
    }
    setTimeout(SlideShow, 5000); // Change image every few seconds
} 

var about = document.getElementsByClassName("aboutStatement")
// console.log(about, "line56")
var aboutptag = [`Lorem ipsum dolor sit amet et delectus 
                    accommodare his consul copiosae legendos 
                    at vix ad putent delectus delicata usu. 
                    Vidit dissentiet eos cu eum an brute 
                    copiosae hendrerit. Eos erant dolorum 
                    an. Per facer affert ut. Mei iisque 
                    mentitum moderatius cu. Sit munere 
                    facilis accusam eu dicat falli consulatu 
                    at vis. Te facilisis mnesarchum qui 
                    posse omnium mediocritatem est cu. Modus 
                    argumentum ne qui tation efficiendi in 
                    eos. Ei mea falli legere efficiantur et 
                    tollit aliquip debitis mei. No deserunt 
                    mediocritatem mel. Lorem ipsum dolor sit 
                    amet et delectus accommodare his consul 
                    copiosae legendos at vix ad putent 
                    delectus delicata usu. Vidit dissentiet 
                    eos cu`,
                    `Lorem ipsum dolor sit amet et delectus 
                    accommodare his consul copiosae legendos 
                    at vix ad putent delectus delicata usu. 
                    Vidit dissentiet eos cu eum an brute 
                    copiosae hendrerit. Eos erant dolorum 
                    an. Per facer affert ut. Mei iisque 
                    mentitum moderatius cu. Sit munere 
                    facilis accusam eu dicat falli consulatu 
                    at vis. Te facilisis mnesarchum qui 
                    posse omnium mediocritatem est cu. Modus 
                    argumentum ne qui tation efficiendi in 
                    eos. Ei mea falli legere efficiantur et 
                    tollit aliquip debitis mei. No deserunt 
                    mediocritatem mel. Lorem ipsum dolor sit 
                    amet et delectus accommodare his consul 
                    copiosae legendos at vix ad putent 
                    delectus delicata usu. Vidit dissentiet 
                    eos cu`,
                    `Lorem ipsum dolor sit amet et delectus 
                    accommodare his consul copiosae legendos 
                    at vix ad putent delectus delicata usu. 
                    Vidit dissentiet eos cu eum an brute 
                    copiosae hendrerit. Eos erant dolorum 
                    an. Per facer affert ut. Mei iisque 
                    mentitum moderatius cu. Sit munere 
                    facilis accusam eu dicat falli consulatu 
                    at vis. Te facilisis mnesarchum qui 
                    posse omnium mediocritatem est cu. Modus 
                    argumentum ne qui tation efficiendi in 
                    eos. Ei mea falli legere efficiantur et 
                    tollit aliquip debitis mei. No deserunt 
                    mediocritatem mel. Lorem ipsum dolor sit 
                    amet et delectus accommodare his consul 
                    copiosae legendos at vix ad putent 
                    delectus delicata usu. Vidit dissentiet 
                    eos cu`]
for (let i = 0; i < about.length; i++) {
    about[i].addEventListener("click", ()=>{
        // console.log(about, "line71")
        if(about[i].classList.contains("fading")){
            for (let i = 0; i < about.length; i++) {
                if(about[i].classList.contains("chosen")){
                    about[i].classList.replace("chosen", "fading")
                }
            }
            about[i].classList.replace("fading", "chosen")
        }
        document.getElementById("aboutPtag").classList.remove("ptagFadingIn")
        document.getElementById("aboutPtag").classList.add("ptagFadingOut")
        setTimeout(()=>{
            console.log(about)
            if(about[0] == about[i]){
                console.log(true)
                document.getElementById("aboutImg").removeAttribute("hidden")
            } else {
                console.log(false)
                document.getElementById("aboutImg").setAttribute("hidden", true)
            }
            document.getElementById("aboutPtag").innerHTML = aboutptag[i]
            document.getElementById("aboutPtag").classList.remove("ptagFadingOut")
            document.getElementById("aboutPtag").classList.add("ptagFadingIn")
        }, 800)
    })
}