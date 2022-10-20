{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPZj4Hy5sVuGoARQe39QJRR",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DaniloPath/pythongeo/blob/main/ListIterection.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "GVI-YZjE23x1"
      },
      "outputs": [],
      "source": [
        "# Interection for list of values\n",
        "\n",
        "# Use assert\n",
        "\n",
        "def num_p_values (value1,value2):\n",
        "  assert type(value1) in [int,float], \"Insert values for 'value1' needs to be integer or floating point number! Found: %s\" % type(value1)\n",
        "  assert type(value2) in [int,float], \"Insert values for 'value2' needs to be integer or floating point number! Found: %s\" % type(value2)\n",
        "\n",
        "  # Check Condictions\n",
        "  assert value1 > 0, \"'value1' needs to be higher than 0! Found %s\" % value1\n",
        "  assert value2 > 0, \"'value2' needs to be higher than 0! Found %s\" % value2\n",
        "  \n",
        "  return value1+value2\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_p_values(1.8,2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-XXTFyJa72Jd",
        "outputId": "eb98cf2d-3272-4ef3-9d22-f03e63252997"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.8"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Using multlists\n",
        "\n",
        "# Create lists\n",
        "cad_imobiliario = ['Antônio Rafael','Maria Rita','Claudionor hoffman']\n",
        "cod_imobiliario = [12,88,55]\n",
        "\n",
        "for personal, cod in zip(cad_imobiliario,cod_imobiliario):\n",
        "  print(personal, 'is propriety of imovel number ', cod)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aNh6DJlv8skk",
        "outputId": "533c3ff6-480b-4acb-d222-6009714b4e32"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Antônio Rafael is propriety of imovel number  12\n",
            "Maria Rita is propriety of imovel number  88\n",
            "Claudionor hoffman is propriety of imovel number  55\n"
          ]
        }
      ]
    }
  ]
}