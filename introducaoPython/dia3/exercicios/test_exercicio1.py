import pytest
from exercicio1 import fizzbuzz
from exercicio1 import translate_to_number
from exercicio1 import validate_email


def test_fizzbuzz_showld_return_list_of_numbers():
    assert fizzbuzz(2) == [1, 2]


def test_divisivel_por_tres():
    assert fizzbuzz(3)[-1] == 'Fizz'


def test_divisivel_por_cinco():
    assert fizzbuzz(5)[-1] == 'Buzz'


def test_divisivel_por_tres_e_cinco():
    assert fizzbuzz(15)[-1] == 'FizzBuzz'


def test_abc_should_be_converted_in_2():
    assert translate_to_number("ABC") == "222"


def test_def_should_be_converted_in_3():
    assert translate_to_number("DEF") == "333"


def test_ghi_should_be_converted_in_4():
    assert translate_to_number("GHI") == "444"


def test_jkl_should_be_converted_in_5():
    assert translate_to_number("JKL") == "555"


def test_mno_should_be_converted_in_6():
    assert translate_to_number("MNO") == "666"


def test_pqrs_should_be_converted_in_7():
    assert translate_to_number("PQRS") == "7777"


def test_tuv_should_be_converted_in_8():
    assert translate_to_number("TUV") == "888"


def test_wxyz_should_be_converted_in_9():
    assert translate_to_number("WXYZ") == "9999"


def test_dash_zero_one_should_be_kept():
    assert translate_to_number("0-1") == "0-1"


def test_expression_should_be_at_least_one_char():
    with pytest.raises(ValueError):
        translate_to_number("")


def test_expression_maximum_are_thirty_chars():
    long_expression = (
        "1111111111"  # 10 chars
        "1111111111"
        "1111111111"
        "1"
    )
    with pytest.raises(ValueError):
        translate_to_number(long_expression)


def test_expression_with_invalid_chars():
    with pytest.raises(ValueError):
        translate_to_number("I-****-MY_JOB")


def test_username_apenas_letras():
    assert validate_email('albertassibenhur@gmail.com') is None


def test_username_letras_digitos():
    assert validate_email('albertassibenhur321@gmail.com') is None


def test_username_letras_digitos_e_pontos():
    assert validate_email('albertassi-benhur@gmail.com') is None


def test_username_letras_digitos_pontos_e_underscores():
    assert validate_email('albertassi_ben-hur@gmail.com') is None


def test_username_comercar_com_letra():
    assert validate_email('albertassibenhur@gmail.com') is None


def test_username_nao_comercar_com_letra():
    with pytest.raises(ValueError):
        validate_email('1albertassibenhur@gmail.com')


def test_username_invalid():
    with pytest.raises(ValueError):
        validate_email('benhur%albertassi@gmail.com')


def test_website_contem_letras_e_digitos():
    assert validate_email('albertassibenhur@gmail123.com') is None


def test_website_invalido():
    with pytest.raises(ValueError):
        validate_email('abc@vdfv!321.com')
