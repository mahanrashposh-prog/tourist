let box_qestiosn=document.getElementById('box_qestiosn')
function get_questions() {
    fetch('http://127.0.0.1:8000/manage/get_sms/').then(
        function (response) {
            return response.json()
            
        }
    ).then(
        function (get_sms) {
            console.log(get_sms)
            
        }
    )
    
}
window.onload=get_questions