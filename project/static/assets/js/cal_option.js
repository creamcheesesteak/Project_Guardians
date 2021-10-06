var result_val = 0.0;
var money_val = 0.0;

function getCheckboxValue(event)  {
  var result = '';
  var money_result = '';

  if(event.target.checked)  {
    result = event.target.value;
    result_val += parseFloat(result);
    document.getElementById('co2').value = Math.round(result_val * 100) / 100;

        switch(event.target.id){
            case 'sol1':
                money_result = document.getElementById('money1').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol2':
                money_result = document.getElementById('money2').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol3':
                money_result = document.getElementById('money3').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol4':
                money_result = document.getElementById('money4').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol5':
                money_result = document.getElementById('money5').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol6':
                money_result = document.getElementById('money6').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol7':
                money_result = document.getElementById('money7').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol8':
                money_result = document.getElementById('money8').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol9':
                money_result = document.getElementById('money9').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol10':
                money_result = document.getElementById('money10').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            }

  }else {
    result2 = event.target.value;
    result_val -= parseFloat(result2);
    document.getElementById('co2').value = Math.round(result_val * 100) / 100;

            switch(event.target.id){
            case 'sol1':
                money_result = document.getElementById('money1').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol2':
                money_result = document.getElementById('money2').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol3':
                money_result = document.getElementById('money3').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol4':
                money_result = document.getElementById('money4').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol5':
                money_result = document.getElementById('money5').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol6':
                money_result = document.getElementById('money6').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol7':
                money_result = document.getElementById('money7').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol8':
                money_result = document.getElementById('money8').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol9':
                money_result = document.getElementById('money9').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            case 'sol10':
                money_result = document.getElementById('money10').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                break;
            }
  }
  //document.getElementById('result').innerText
  // = result;
}
