$(document).ready(function(){
    $('body #lista').on('click', '.item', function(){

        let id = $(this).attr('id');
        let elemento = document.getElementById(id);

        Swal.fire({
          title: "Registrar",      
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Apoyo',
          cancelButtonText: 'Falta'
        }).then((result) => {
            
            let validacion = result.isConfirmed
           
            if (validacion){
                if (elemento.style.backgroundColor == "blue"){
                        elemento.style.backgroundColor = "";
                }
                else {
                    elemento.style.backgroundColor = "blue";
                }
            }
            else {
                if (result.dismiss == "cancel"){
                    if (elemento.style.backgroundColor == "red"){
                        elemento.style.backgroundColor = "";
                    }
                    else {
                    elemento.style.backgroundColor = "red";
                    }
                }
            }

              
        });
      })       
    });

