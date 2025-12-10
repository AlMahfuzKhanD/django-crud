<template>
  <div class="min-h-screen bg-gray-100 py-6 px-4 sm:px-6 lg:px-8">
    <div class="container mx-auto max-w-7xl">
      <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold mb-6 text-gray-800 text-center">Employee Management</h1>

      <!-- Form -->
      <div class="bg-white shadow rounded-lg p-6 sm:p-8 mb-6">
        <h2 class="text-lg sm:text-xl font-semibold mb-6 text-gray-800">{{ editingId ? 'Edit Employee' : 'Add Employee' }}</h2>
        
        <form @submit.prevent="saveEmployee" class="space-y-4">
          <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            <div>
              <label class="block text-sm font-medium mb-1 text-gray-700">Name</label>
              <input
                v-model="form.name"
                type="text"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-base"
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium mb-1 text-gray-700">Mobile</label>
              <input
                v-model="form.mobile"
                type="text"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            
            <div class="md:col-span-2 xl:col-span-1">
              <label class="block text-sm font-medium mb-1 text-gray-700">Area</label>
              <input
                v-model="form.area"
                type="text"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
          </div>
          
          <div class="flex flex-wrap gap-2">
            <button
              type="submit"
              class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
            >
              {{ editingId ? 'Update' : 'Add' }}
            </button>
            <button
              v-if="editingId"
              @click="cancelEdit"
              type="button"
              class="px-6 py-2.5 bg-gray-300 text-gray-700 rounded hover:bg-gray-400 transition text-base font-medium"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>

      <!-- Employee List -->
      <div class="bg-white shadow rounded-lg overflow-hidden">
        <div class="px-4 sm:px-6 py-4 bg-gray-50 border-b">
          <h2 class="text-lg sm:text-xl font-semibold text-gray-800">Employee List ({{ employees.length }})</h2>
        </div>
        
        <div v-if="employees.length > 0" class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50 border-b">
              <tr>
                <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 w-1/4">Name</th>
                <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 w-1/4">Mobile</th>
                <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 w-1/4">Area</th>
                <th class="px-6 py-4 text-center text-sm font-semibold text-gray-700 w-1/4">Actions</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              <tr v-for="emp in employees" :key="emp.id" class="hover:bg-gray-50 transition">
                <td class="px-6 py-4 text-gray-800 text-base">{{ emp.name }}</td>
                <td class="px-6 py-4 text-gray-600 text-base">{{ emp.mobile }}</td>
                <td class="px-6 py-4 text-gray-600 text-base">{{ emp.area }}</td>
                <td class="px-6 py-4">
                  <div class="flex justify-center gap-3">
                    <button
                      @click="editEmployee(emp)"
                      class="px-4 py-2 bg-yellow-500 text-white text-sm font-medium rounded hover:bg-yellow-600 transition"
                    >
                      Edit
                    </button>
                    <button
                      @click="deleteEmployee(emp.id)"
                      class="px-4 py-2 bg-red-500 text-white text-sm font-medium rounded hover:bg-red-600 transition"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <div v-else class="px-4 sm:px-6 py-12 text-center text-gray-500">
          No employees found. Add one using the form above.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../services/api';

const employees = ref([]);
const editingId = ref(null);

const form = ref({
  name: '',
  mobile: '',
  area: ''
});

const fetchEmployees = async () => {
  try {
    const res = await api.get('employees/');
    employees.value = res.data;
  } catch (error) {
    console.error('Error fetching employees:', error);
  }
};

const saveEmployee = async () => {
  try {
    if (editingId.value) {
      await api.put(`employees/${editingId.value}/`, form.value);
      editingId.value = null;
    } else {
      await api.post('employees/', form.value);
    }
    form.value = { name: '', mobile: '', area: '' };
    fetchEmployees();
  } catch (error) {
    console.error('Error saving employee:', error);
  }
};

const editEmployee = (emp) => {
  form.value = { name: emp.name, mobile: emp.mobile, area: emp.area };
  editingId.value = emp.id;
};

const cancelEdit = () => {
  editingId.value = null;
  form.value = { name: '', mobile: '', area: '' };
};

const deleteEmployee = async (id) => {
  if (confirm('Are you sure you want to delete this employee?')) {
    try {
      await api.delete(`employees/${id}/`);
      fetchEmployees();
    } catch (error) {
      console.error('Error deleting employee:', error);
    }
  }
};

onMounted(() => {
  fetchEmployees();
});
</script>