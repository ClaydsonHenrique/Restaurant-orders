# Restaurant Orders

## Descrição do Projeto
Este projeto visa implementar testes para classes já existentes e desenvolver novas funcionalidades para a gestão de pratos e ingredientes no restaurante 🍝 🦐 Chapa Quente 🍛 🥘. O projeto inclui o mapeamento de pratos e ingredientes, geração de cardápios dinâmicos com base em restrições alimentares e disponibilidade de estoque, além de controle de estoque.

## Funcionalidades Implementadas

### 1. Testando a Classe `Ingredient` (`tests/ingredient/test_ingredient.py`)
- **Objetivo:** Implementar testes para a classe `Ingredient` que representa ingredientes.
- **Verificações:**
  - Instanciação correta da classe.
  - Atributo `restrictions` populado corretamente.
  - Funcionamento dos métodos mágicos `__repr__`, `__eq__` e `__hash__`.

### 2. Testando a Classe `Dish` (`tests/dish/test_dish.py`)
- **Objetivo:** Implementar testes para a classe `Dish` que representa pratos do cardápio.
- **Verificações:**
  - Instanciação correta da classe.
  - Funcionamento dos métodos da classe, incluindo métodos mágicos.
  - Dicionário de receita do prato com a quantidade correta de ingredientes.
  - Levantamento de erros ao criar pratos inválidos.

### 3. Mapeamento de Pratos e Ingredientes (`src/services/menu_data.py`)
- **Classe `MenuData`:**
  - Leitura de arquivo CSV contendo pratos e ingredientes.
  - Instanciação correta de pratos e ingredientes.
  - Atributo `dishes` contendo um set de pratos instanciados.
  - Relacionamento correto dos pratos com suas receitas e preços.

### 4. Geração de Cardápios Dinâmicos (`src/services/menu_builder.py`)
- **Classe `MenuBuilder`:**
  - Método `get_main_menu` para geração de cardápios dinâmicos.
  - Retorno de lista de dicionários com os pratos, ingredientes, preço e restrições.
  - Filtragem de pratos com base em restrições alimentares.

### 5. Controle de Estoque de Ingredientes (`src/services/inventory_control.py`)
- **Classe `InventoryMapping`:**
  - Método `check_recipe_availability` para verificar disponibilidade de receitas no estoque.
  - Método `consume_recipe` para subtrair ingredientes do estoque ao consumir uma receita.

### 6. Cardápios Baseados no Estoque (`src/services/menu_builder.py`)
- **Complemento ao Método `get_main_menu`:**
  - Consideração da disponibilidade de ingredientes no estoque ao gerar cardápios.
  - Filtragem de pratos com base em restrições alimentares e disponibilidade de ingredientes.
