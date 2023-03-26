const deleteButton = document.getElementById('delete')
const setButton = document.getElementById('set')

deleteButton.addEventListener("click", () =>{
    const elements = document.querySelectorAll('header,h1,h2,aside,nav,main,footer,li,blockquote,p,form,input');
    elements.forEach(element => {
        element.classList.add('unset');
        element.classList.remove('azure');
    })
})

setButton.addEventListener("click",()=>{
    const elements = document.querySelectorAll('header,h1,h2,aside,nav,main,footer,li,blockquote,p,form,input');
    elements.forEach(element =>{
        element.classList.remove('unset');
    })
    const azureElements = document.querySelectorAll('nav,aside, main, form, footer');
    azureElements.forEach(element =>{
        element.classList.add('azure');
    })
})


// another way to do the same thing
// let styles = document.styleSheets;
//
// console.log(styles)
//
// document.getElementById('delete').onclick = () => {
//     styles[0].disabled = true;
// }
//
// document.getElementById('set').onclick = () => {
//     styles[0].disabled = false;
// }