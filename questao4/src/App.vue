<template>
  <div class="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
    <div class="relative py-3 sm:max-w-4xl sm:mx-auto">
      <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
        <div class="max-w-3xl mx-auto">
          <div class="divide-y divide-gray-200">
            <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
              <h1 class="text-2xl font-bold mb-8 text-center text-blue-600">
                Busca de Operadoras de Saúde
              </h1>
              
              <!-- Search Input -->
              <div class="relative mb-8">
                <input 
                  type="text" 
                  v-model="searchQuery"
                  @input="searchOperators"
                  placeholder="Digite para buscar operadoras..."
                  class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                />
              </div>

              <!-- Loading State -->
              <div v-if="loading" class="text-center py-4">
                <p>Buscando...</p>
              </div>

              <!-- Results -->
              <div v-if="results.length > 0" class="mt-6">
                <div v-for="(operator, index) in results" 
                     :key="index"
                     class="mb-6 p-6 border rounded-lg hover:bg-gray-50">
                  
                  <!-- Basic Information -->
                  <div class="mb-4">
                    <h3 class="font-bold text-xl text-blue-600">{{ operator.nome_fantasia }}</h3>
                    <p class="text-md text-gray-600">{{ operator.razao_social }}</p>
                  </div>

                  <!-- Detailed Information -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                    <div>
                      <h4 class="font-semibold text-gray-700 mb-2">Informações Básicas</h4>
                      <p><span class="font-semibold">CNPJ:</span> {{ operator.cnpj }}</p>
                      <p><span class="font-semibold">Modalidade:</span> {{ operator.modalidade }}</p>
                      <p><span class="font-semibold">Data Registro ANS:</span> {{ operator.data_registro_ans }}</p>
                      <p><span class="font-semibold">Região de Comercialização:</span> {{ operator.regiao_de_comercializacao }}</p>
                    </div>

                    <div>
                      <h4 class="font-semibold text-gray-700 mb-2">Endereço</h4>
                      <p>{{ operator.logradouro }}, {{ operator.numero }}</p>
                      <p v-if="operator.complemento">{{ operator.complemento }}</p>
                      <p>{{ operator.bairro }}</p>
                      <p>{{ operator.cidade }} - {{ operator.uf }}</p>
                      <p>CEP: {{ operator.cep }}</p>
                    </div>

                    <div>
                      <h4 class="font-semibold text-gray-700 mb-2">Contato</h4>
                      <p v-if="operator.telefone"><span class="font-semibold">Telefone:</span> ({{ operator.ddd }}) {{ operator.telefone }}</p>
                      <p v-if="operator.fax"><span class="font-semibold">Fax:</span> ({{ operator.ddd }}) {{ operator.fax }}</p>
                      <p v-if="operator.endereco_eletronico"><span class="font-semibold">Email:</span> {{ operator.endereco_eletronico }}</p>
                    </div>

                    <div>
                      <h4 class="font-semibold text-gray-700 mb-2">Representante</h4>
                      <p><span class="font-semibold">Nome:</span> {{ operator.representante }}</p>
                      <p><span class="font-semibold">Cargo:</span> {{ operator.cargo_representante }}</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- No Results -->
              <div v-if="!loading && searchQuery && results.length === 0" class="text-center py-4">
                <p>Nenhuma operadora encontrada.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'App',
  setup() {
    const searchQuery = ref('')
    const results = ref([])
    const loading = ref(false)

    let timeout = null

    const searchOperators = async () => {
      clearTimeout(timeout)
      
      if (searchQuery.value.length < 2) {
        results.value = []
        return
      }

      timeout = setTimeout(async () => {
        try {
          loading.value = true
          const response = await axios.get(`http://localhost:5000/api/search?q=${encodeURIComponent(searchQuery.value)}`)
          results.value = response.data
        } catch (error) {
          console.error('Error searching operators:', error)
          results.value = []
        } finally {
          loading.value = false
        }
      }, 300)
    }

    return {
      searchQuery,
      results,
      loading,
      searchOperators
    }
  }
}
</script>