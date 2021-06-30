<template>
    <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">

            <v-btn block elevation="0" color="primary" v-bind="attrs" v-on="on">
                Продать
            </v-btn>

        </template>
        <v-card class="pt-0 pb-4">
            <v-card-title>
                <v-btn tile icon @click="dialog = false">
                    <v-icon>mdi-close</v-icon>
                </v-btn>
            </v-card-title>
            <v-card-text>
                <v-row>
                    <v-col cols="12">
                                        <v-card outlined class="">
                                            <v-card-text class="">
                                                <v-row no-gutters>
                                                    <v-col class="d-flex align-center">
                                                        <v-list-item-avatar class="ma-0 mr-5">
                                                            <v-icon class="grey lighten-1" dark> mdi-note-text-outline
                                                            </v-icon>
                                                        </v-list-item-avatar>
                                                        <h1 class="text-subtitle-2">OZON</h1>
                                                    </v-col>
                                                    <v-col
                                                        class="d-flex align-center justify-end text-center text-sm-end">
                                                        <p
                                                            class="mt-5 mt-sm-0 text-caption text-sm-subtitle-1 ma-0 text-no-wrap">
                                                            39 810,63₮ → 40 810,63₮ </p>
                                                    </v-col>
                                                </v-row>
                                            </v-card-text>
                                        </v-card>
                                
                    </v-col>
                    <v-col cols="12">
                        <v-text-field outlined label="Legal middle name" hint="example of helper text only on focus">
                        </v-text-field>
                    </v-col>
                    <v-col>
                        <v-btn block elevation="0" color="primary" text @click="dialog = false">
                            Продать
                        </v-btn>
                    </v-col>
                </v-row>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        data: () => ({
            dialog: false,
            model: ''
        })
    }
</script>

<style>

</style>