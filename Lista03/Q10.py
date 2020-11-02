
$limiteInferior = intval(readline('Valor do limite inferior: '));
$limiteSuperior = intval(readline('Valor do limite superior: '));



for ($i=$limiteInferior; $i <= $limiteSuperior; $i++) { 
    if($i % 2 === 0){   
        echo "Valor Par : $i\n";
    }
    
}
