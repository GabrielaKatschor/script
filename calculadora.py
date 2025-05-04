{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "op = ''\n",
        "result = 0\n",
        "num1 = 0\n",
        "num2 = 0\n",
        "\n",
        "\n",
        "print('Olá, seja bem vindo a calculadora')\n",
        "print('Por favor digite dois números:')\n",
        "num1 = float(input('Digite o primeiro número '))\n",
        "num2 = float(input('Digite o segundo número '))\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "print('Digite + para adição')\n",
        "print('Digite - para subtração')\n",
        "print('Digite * para multiplicação')\n",
        "print('Digite / para divisão')\n",
        "op = (input('Digite a operação desejada: '))\n",
        "\n",
        "\n",
        "if  op=='+':\n",
        "       result= num1 + num2\n",
        "elif op=='-':\n",
        "      result= num1 - num2\n",
        "elif op=='*':\n",
        "      result= num1 * num2\n",
        "elif op=='/':\n",
        "    result= num1 / num2\n",
        "\n",
        "\n",
        "\n",
        "print ('O resultado é:' '{} {} {} = {}'.format(num1, op, num2,result))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "EZCYZWJmOHJy",
        "outputId": "41809b7c-edf6-4e65-9980-0e328aff657e"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, seja bem vindo a calculadora\n",
            "Por favor digite dois números:\n",
            "Digite o primeiro número 5\n",
            "Digite o segundo número 10\n",
            "Digite + para adição\n",
            "Digite - para subtração\n",
            "Digite * para multiplicação\n",
            "Digite / para divisão\n",
            "Digite a operação desejada: -\n",
            "O resultado é:5.0 - 10.0 = -5.0\n"
          ]
        }
      ]
    }
  ]
}
