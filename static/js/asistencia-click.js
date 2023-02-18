$(document).ready( function(){
    $('body #lista').on('click', 'td', async function(){    
        id =  $(this).attr('id');
        var elemento = document.getElementById(id);

        Swal.fire({
          title: "Registrar",
          text: "Apoyo y/o Falta",         
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Si',
          cancelButtonText: 'No'
        }).then((result) => {

            if(result.value){
                if (elemento.style.backgroundColor == ""){
                    elemento.style.backgroundColor = "blue";
                }   
                else if (elemento.style.backgroundColor == "blue"){
                    elemento.style.backgroundColor = "red";        
                }
                else if (elemento.style.backgroundColor == "red"){
                    elemento.style.backgroundColor = "";        
                }             
            }         
        });
      })       
    }
  );

