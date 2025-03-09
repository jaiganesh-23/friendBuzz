<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="space-y-4">
                    <div 
                        class="flex items-center justify-between"
                        v-for="conversation in conversations"
                        v-bind:key="conversation.id"
                        v-on:click="setActiveConversation(conversation.id)"
                    >
                        <div class="flex items-center space-x-2">
                            <template
                                v-for="user in conversation.users"
                                v-bind:key="user.id"
                            >
                                <img :src="user.get_avatar" class="w-[40px] rounded-full" v-if="user.id !== userStore.user.id">
                                <p 
                                    class="text-xs font-bold"
                                    v-if="user.id !== userStore.user.id"
                                >{{ user.name }}</p>
                            </template>
                        </div>
                        <span class="text-xs text-gray-500">{{ conversation.modified_at_formatted }} ago</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg h-[60vh] overflow-y-auto" ref="chatContainer">
                <div class="flex flex-col flex-grow p-4">
                    <template
                        v-for="message in activeConversation.messages"
                        v-bind:key="message.id"
                    >
                        <div 
                            class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end"
                            v-if="message.created_by.id == userStore.user.id"
                        >
                            <div>
                                <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                    <p class="text-sm">{{ message.body }}</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">{{ message.created_at_formatted }} ago</span>
                            </div>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img :src="message.created_by.get_avatar" class="w-[40px] rounded-full">
                            </div>
                        </div>

                        <div 
                            class="flex w-full mt-2 space-x-3 max-w-md"
                            v-else
                        >
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img :src="message.created_by.get_avatar" class="w-[40px] rounded-full">
                            </div>
                            <div>
                                <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                                    <p class="text-sm">{{ message.body }}</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">{{ message.created_at_formatted }} ago</span>
                            </div>
                        </div>
                    </template>
                </div>
            </div>

            <div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm">
                    <div class="p-4">  
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What do you want to say?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Send</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { io } from 'socket.io-client'

export default {
    name: 'chat',

    setup() {
        const userStore = useUserStore()
        const socket = io(import.meta.env.VITE_API_URL)
        socket.on("connect", ()=> {
            socket.emit("connection_event", {message1: "hello", message2: "hello2"});
        })
        socket.on("connection_response", (message)=>{
            console.log('inside connection response')
            console.log(message)
        })
        return {
            userStore,
            socket,
        }
    },

    data() {
        return {
            conversations: [],
            activeConversation: {},
            body: '',
            activeConversationId: '',
        }
    },

    mounted() {
        this.getConversations()
        this.socket.connect();
        this.socket.on("message_response", (message)=> {
            if(message.conversation.id == this.activeConversationId && message.created_by.id != this.userStore.user.id){
                    console.log('inside final add');
                    console.log(message);
                    this.activeConversation.messages.push(message);
                    this.scrollToBottom();
                }
            })
        this.scrollToBottom();
    },
    
    methods: {
        setActiveConversation(id) {
            console.log('setActiveConversation', id)

            this.activeConversation = id
            this.activeConversationId = id
            this.getMessages()
            this.scrollToBottom()
        },
        getConversations() {
            console.log('getConversations')

            axios
                .get('/api/chat/')
                .then(response => {
                    console.log(response.data)

                    this.conversations = response.data

                    if (this.conversations.length) {
                        this.activeConversation = this.conversations[0].id
                        this.activeConversationId = this.conversations[0].id
                    }

                    this.getMessages()
                })
                .catch(error => {
                    console.log(error)
                })
        },

        getMessages() {
            console.log('getMessages')

            axios
                .get(`/api/chat/${this.activeConversation}/`)
                .then(response => {
                    console.log(response.data)
                    this.activeConversationId = this.activeConversation
                    this.activeConversation = response.data
                    this.scrollToBottom();
                })
                .catch(error => {
                    console.log(error)
                })
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post(`/api/chat/${this.activeConversation.id}/send/`, {
                    body: this.body
                })
                .then(response => {
                    console.log(response.data)
                    this.socket.emit("my_message", response.data)
                    this.activeConversation.messages.push(response.data)
                    this.body = ''
                    this.scrollToBottom();
                })
                .catch(error => {
                    console.log(error)
                })
        },

        scrollToBottom() {
            this.$nextTick(() => {
                const chatContainer = this.$refs.chatContainer;
                chatContainer.scrollTop = chatContainer.scrollHeight;
            });
        }
    }
}
</script>