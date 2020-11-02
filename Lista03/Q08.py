
$N = intval(readline('Valor de N: '));
$limiteInferior = intval(readline('Valor do limite inferior: '));
$limiteSuperior = intval(readline('Valor do limite superior: '));


for ($i=$limiteInferior; $i <= $limiteSuperior; $i++) { 
    echo "Valor múltiplo : ". ($i * $N) . "\n";
}




?>
