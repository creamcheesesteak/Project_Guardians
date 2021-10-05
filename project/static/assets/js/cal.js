function call()
        {
         if(document.getElementById("elec").value && document.getElementById("cell2").value){
          document.getElementById('co2').value =parseInt(document.getElementById('elec').value) + parseInt(document.getElementById('cell2').value);
         }
        }
        function call2()
        {
         if(document.getElementById("elec").value){
          document.getElementById('tree').value = Math.round((((parseInt(document.getElementById('elec').value)  * 0.4663)/ 6.6) / 0.1) * 0.1);
         }{
          document.getElementById('co2').value = (Math.round((parseInt(document.getElementById('elec').value)  * 0.4663) / 0.1)) * 0.1;
         }
        }