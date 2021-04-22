<template>
  <q-page padding>
    <button v-on:click="getItems()">Recargar</button>
    <q-list>
      <q-expansion-item 
        v-for="item in items" :key="item.id"
        popup
        group="items"
        :label="`Item ${item.id}:: ${item.nombre}`"
      >
        <q-card>
          <q-form :action="`/item/${item.id}`" method="PUT" @submit="enviar">
            <q-input  v-model="item.nombre"     name="nombre"     label="Nombre"
              :rules="[
                val => val && val.length > 0 || 'Campo no puede estar vacio',
                val => val.length < 20 || 'Nombre no puede tener más de 20 caracteres'
              ]" 
            />
            <q-input  v-model="item.valor"      name="valor"      label="Valor" type="number"
              :rules="[
                val => val !== null && val !== '' || 'Debe incluir un valor',
                val => val >= 0 && val < 65535 || 'Valor ha de ser positivo menor a 65535'
              ]"
            />
            <q-toggle v-model="item.disponible" name="disponible" label="Disponible" />
            <br>
            <q-btn label="Actualizar" type="submit" />
            <q-btn label="Borrar" @click="borrar(item.id)" />
          </q-form>
        </q-card>
      </q-expansion-item>
      <q-expansion-item 
        popup
        group="items"
        label="Nuevo"
      >
        <q-card>
          <q-form action="/items" method="POST" @submit="crear">
            <q-input  v-model="nuevo.nombre"      name="nombre"     label="Nombre" lazy-rules 
              :rules="[
                val => val && val.length > 0 || 'Campo no puede estar vacio',
                val => val.length < 20 || 'Nombre no puede tener más de 20 caracteres'
              ]" 
            />
            <q-input  v-model="nuevo.valor"       name="valor"      label="Valor" type="number" lazy-rules
              :rules="[
                val => val !== null && val !== '' || 'Debe incluir un valor',
                val => val >= 0 && val < 65535 || 'Valor ha de ser positivo menor a 65535'
              ]"
            />
            <q-toggle v-model="nuevo.disponible"  name="disponible" label="Disponible" />
            <br>
            <q-btn label="Crear" type="submit" />
          </q-form>
        </q-card>
      </q-expansion-item>
    </q-list>
  </q-page>
</template>

<script>
// import { Item } from 'components/models'
import $ from 'jquery';

export default {
  name: 'PageName',
  data() {
    return { 
      url: '',
      nuevo: { nombre: '', valor: 0, disponible: false },
      items: []
    }
  },
  methods: {
    borrar(item = 0) {
      this.$api.delete(`/item/${item}`)
        .then(() => { 
          this.getItems() 
          this.$q.notify({
            color: 'blue',
            textColor: 'white',
            message: 'Borrado satifactoriamente'
          })
        })
        .catch(err => { console.error(err) })
    },
    crear(evt) {
      this.enviar(evt);
      this.nuevo = { nombre: '', valor: 0, disponible: false };
      evt.target.reset();
    },
    enviar(evt) {
      const form = $(evt.target);
      console.log(form.serialize());
      this.$api({
        method: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize()
      }).then(() => { 
        this.getItems();
        this.$q.notify({
          color: 'green',
          textColor: 'white',
          message: 'Item actualizado exitosamente'
        })
      }).catch(err => {
        console.error(err);
        this.$q.notify({
          color: 'red',
          textColor: 'white',
          message: 'Error, datos inválidos'
        })
      })
    },
    async getItems() {
      try {
        const resp = await this.$api.get('/items'); 
        this.items = resp.data.items;
        this.items.forEach(item => { item.disponible = item.disponible !== 0 })
      } catch (err) { 
        console.error(err) 
      }
    },
    updateItem() { return 0; }
  },
  mounted() {
    this.getItems();
  }
}
</script>
