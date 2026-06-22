
async function askQuestion(){

    let question =
    document.getElementById("question").value;


    let response = await fetch(
        "http://127.0.0.1:8000/chat",
        {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                question:question

            })

        }
    );


    let data = await response.json();


    document.getElementById("chatBox").innerHTML =
    data.answer;

}