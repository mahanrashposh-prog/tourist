let users=document.getElementById('users')
let question=document.getElementById('question')
function user() {
    window.location.assign('users/users.html')
    
}
users.addEventListener('click',user)
function all_question() {
    window.location.assign('qestiosn/qestiosn.html')
    
}
question.addEventListener('click',all_question)