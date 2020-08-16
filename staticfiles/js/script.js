document.addEventListener("DOMContentLoaded", function () {
    console.log("hi");
})

function scrollTo(obj){
    obj.scrollIntoView({block: "start",  behavior: "smooth"});
}
