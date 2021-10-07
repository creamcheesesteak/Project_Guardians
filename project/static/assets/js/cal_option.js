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
                document.getElementById('no1').value = document.getElementById('no_1').value;
                break;
            case 'sol2':
                money_result = document.getElementById('money2').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('no2').value = document.getElementById('no_2').value;
                break;
            case 'sol3':
                money_result = document.getElementById('money3').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('no3').value = document.getElementById('no_3').value;
                break;
            case 'sol4':
                money_result = document.getElementById('money4').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('no4').value = document.getElementById('no_4').value;
                break;
            case 'sol5':
                money_result = document.getElementById('money5').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('no5').value = document.getElementById('no_5').value;
                break;
            case 'sol6':
                money_result = document.getElementById('money6').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no1').value = document.getElementById('fuel__no1').value;
                break;
            case 'sol7':
                money_result = document.getElementById('money7').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no2').value = document.getElementById('fuel__no2').value;
                break;
            case 'sol8':
                money_result = document.getElementById('money8').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no3').value = document.getElementById('fuel__no3').value;
                break;
            case 'sol9':
                money_result = document.getElementById('money9').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no4').value = document.getElementById('fuel__no4').value;
                break;
            case 'sol10':
                money_result = document.getElementById('money10').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no5').value = document.getElementById('fuel__no5').value;
                break;
            case 'sol11':
                money_result = document.getElementById('money11').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no1').value = document.getElementById('elec__no1').value;
                break;
            case 'sol12':
                money_result = document.getElementById('money12').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no2').value = document.getElementById('elec__no2').value;
                break;
            case 'sol13':
                money_result = document.getElementById('money13').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no3').value = document.getElementById('elec__no3').value;
                break;
            case 'sol14':
                money_result = document.getElementById('money14').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no4').value = document.getElementById('elec__no4').value;
                break;
            case 'sol15':
                money_result = document.getElementById('money15').value;
                money_val += parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no5').value = document.getElementById('elec__no5').value;
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
                document.getElementById('no1').value = null;
                break;
            case 'sol2':
                money_result = document.getElementById('money2').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('no2').value = null;
                break;
            case 'sol3':
                money_result = document.getElementById('money3').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('no3').value = null;
                break;
            case 'sol4':
                money_result = document.getElementById('money4').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('no4').value = null;
                break;
            case 'sol5':
                money_result = document.getElementById('money5').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('no5').value = null;
                break;
            case 'sol6':
                money_result = document.getElementById('money6').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no1').value = null;
                break;
            case 'sol7':
                money_result = document.getElementById('money7').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no2').value = null;
                break;
            case 'sol8':
                money_result = document.getElementById('money8').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no3').value = null;
                break;
            case 'sol9':
                money_result = document.getElementById('money9').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no4').value = null;
                break;
            case 'sol10':
                money_result = document.getElementById('money10').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('fuel_no5').value = null;
                break;
            case 'sol11':
                money_result = document.getElementById('money11').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no1').value = null;
                break;
            case 'sol12':
                money_result = document.getElementById('money12').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no2').value = null;
                break;
            case 'sol13':
                money_result = document.getElementById('money13').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no3').value = null;
                break;
            case 'sol14':
                money_result = document.getElementById('money14').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no4').value = null;
                break;
            case 'sol15':
                money_result = document.getElementById('money15').value;
                money_val -= parseFloat(money_result);
                document.getElementById('money').value = Math.round(money_val * 100) / 100;
                document.getElementById('elec_no5').value = null;
                break;
            }
  }
  //document.getElementById('result').innerText
  // = result;
}
