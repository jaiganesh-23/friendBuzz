<template>
    <nav class="px-5 border-b border-gray-200">
            <div class="flex items-center justify-between">
                <div class="menu-left">
                    <RouterLink to="/" class="text-2xl py-4">FriendBuzz</RouterLink>
                </div>

                <div class="menu-center flex space-x-12" v-if="userStore.user.isAuthenticated">
                    <RouterLink to="/feed" active-class="active" class="py-4">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-10">
                            <path d="M11.47 3.841a.75.75 0 0 1 1.06 0l8.69 8.69a.75.75 0 1 0 1.06-1.061l-8.689-8.69a2.25 2.25 0 0 0-3.182 0l-8.69 8.69a.75.75 0 1 0 1.061 1.06l8.69-8.689Z" />
                            <path d="m12 5.432 8.159 8.159c.03.03.06.058.091.086v6.198c0 1.035-.84 1.875-1.875 1.875H15a.75.75 0 0 1-.75-.75v-4.5a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75V21a.75.75 0 0 1-.75.75H5.625a1.875 1.875 0 0 1-1.875-1.875v-6.198a2.29 2.29 0 0 0 .091-.086L12 5.432Z" />
                        </svg>

                    </RouterLink>

                    <RouterLink to="/chat" active-class="active" class="py-4">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-10">
                            <path fill-rule="evenodd" d="M12 2.25c-2.429 0-4.817.178-7.152.521C2.87 3.061 1.5 4.795 1.5 6.741v6.018c0 1.946 1.37 3.68 3.348 3.97.877.129 1.761.234 2.652.316V21a.75.75 0 0 0 1.28.53l4.184-4.183a.39.39 0 0 1 .266-.112c2.006-.05 3.982-.22 5.922-.506 1.978-.29 3.348-2.023 3.348-3.97V6.741c0-1.947-1.37-3.68-3.348-3.97A49.145 49.145 0 0 0 12 2.25ZM8.25 8.625a1.125 1.125 0 1 0 0 2.25 1.125 1.125 0 0 0 0-2.25Zm2.625 1.125a1.125 1.125 0 1 1 2.25 0 1.125 1.125 0 0 1-2.25 0Zm4.875-1.125a1.125 1.125 0 1 0 0 2.25 1.125 1.125 0 0 0 0-2.25Z" clip-rule="evenodd" />
                        </svg>      
                    </RouterLink>

                    <RouterLink to="/notifications" active-class="active" class="py-4">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-10">
                            <path fill-rule="evenodd" d="M5.25 9a6.75 6.75 0 0 1 13.5 0v.75c0 2.123.8 4.057 2.118 5.52a.75.75 0 0 1-.297 1.206c-1.544.57-3.16.99-4.831 1.243a3.75 3.75 0 1 1-7.48 0 24.585 24.585 0 0 1-4.831-1.244.75.75 0 0 1-.298-1.205A8.217 8.217 0 0 0 5.25 9.75V9Zm4.502 8.9a2.25 2.25 0 1 0 4.496 0 25.057 25.057 0 0 1-4.496 0Z" clip-rule="evenodd" />
                        </svg>    
                    </RouterLink>

                    <RouterLink to="/search" active-class="active" class="py-4">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-10">
                            <path d="M8.25 10.875a2.625 2.625 0 1 1 5.25 0 2.625 2.625 0 0 1-5.25 0Z" />
                            <path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25Zm-1.125 4.5a4.125 4.125 0 1 0 2.338 7.524l2.007 2.006a.75.75 0 1 0 1.06-1.06l-2.006-2.007a4.125 4.125 0 0 0-3.399-6.463Z" clip-rule="evenodd" />
                        </svg>                                
                    </RouterLink>
                </div>

                
                <template v-if="userStore.user.isAuthenticated && userStore.user.id">
                    <div class="menu-right">
                        <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}" class="py-4">
                            <img :src="userStore.user.avatar" class="w-12 rounded-full">
                        </RouterLink>
                    </div>
                </template>

                <template v-else>
                    <div class="menu-right flex space-x-6 items-center w-fit text-xl">
                        <RouterLink to="/" active-class="active" class="flex items-center space-x-1 py-4">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                <path d="M11.47 3.841a.75.75 0 0 1 1.06 0l8.69 8.69a.75.75 0 1 0 1.06-1.061l-8.689-8.69a2.25 2.25 0 0 0-3.182 0l-8.69 8.69a.75.75 0 1 0 1.061 1.06l8.69-8.689Z" />
                                <path d="m12 5.432 8.159 8.159c.03.03.06.058.091.086v6.198c0 1.035-.84 1.875-1.875 1.875H15a.75.75 0 0 1-.75-.75v-4.5a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75V21a.75.75 0 0 1-.75.75H5.625a1.875 1.875 0 0 1-1.875-1.875v-6.198a2.29 2.29 0 0 0 .091-.086L12 5.432Z" />
                            </svg>
                            Home
                        </RouterLink>
                        <RouterLink to="/login" active-class="active" class="flex items-center space-x-1 py-4">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                <path fill-rule="evenodd" d="M9 1.5H5.625c-1.036 0-1.875.84-1.875 1.875v17.25c0 1.035.84 1.875 1.875 1.875h12.75c1.035 0 1.875-.84 1.875-1.875V12.75A3.75 3.75 0 0 0 16.5 9h-1.875a1.875 1.875 0 0 1-1.875-1.875V5.25A3.75 3.75 0 0 0 9 1.5Zm6.61 10.936a.75.75 0 1 0-1.22-.872l-3.236 4.53L9.53 14.47a.75.75 0 0 0-1.06 1.06l2.25 2.25a.75.75 0 0 0 1.14-.094l3.75-5.25Z" clip-rule="evenodd" />
                                <path d="M12.971 1.816A5.23 5.23 0 0 1 14.25 5.25v1.875c0 .207.168.375.375.375H16.5a5.23 5.23 0 0 1 3.434 1.279 9.768 9.768 0 0 0-6.963-6.963Z" />
                            </svg>
                            Login
                        </RouterLink>
                        <RouterLink to="/signup" active-class="active" class="flex items-center space-x-1 py-4">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                <path fill-rule="evenodd" d="M7.502 6h7.128A3.375 3.375 0 0 1 18 9.375v9.375a3 3 0 0 0 3-3V6.108c0-1.505-1.125-2.811-2.664-2.94a48.972 48.972 0 0 0-.673-.05A3 3 0 0 0 15 1.5h-1.5a3 3 0 0 0-2.663 1.618c-.225.015-.45.032-.673.05C8.662 3.295 7.554 4.542 7.502 6ZM13.5 3A1.5 1.5 0 0 0 12 4.5h4.5A1.5 1.5 0 0 0 15 3h-1.5Z" clip-rule="evenodd" />
                                <path fill-rule="evenodd" d="M3 9.375C3 8.339 3.84 7.5 4.875 7.5h9.75c1.036 0 1.875.84 1.875 1.875v11.25c0 1.035-.84 1.875-1.875 1.875h-9.75A1.875 1.875 0 0 1 3 20.625V9.375ZM6 12a.75.75 0 0 1 .75-.75h.008a.75.75 0 0 1 .75.75v.008a.75.75 0 0 1-.75.75H6.75a.75.75 0 0 1-.75-.75V12Zm2.25 0a.75.75 0 0 1 .75-.75h3.75a.75.75 0 0 1 0 1.5H9a.75.75 0 0 1-.75-.75ZM6 15a.75.75 0 0 1 .75-.75h.008a.75.75 0 0 1 .75.75v.008a.75.75 0 0 1-.75.75H6.75a.75.75 0 0 1-.75-.75V15Zm2.25 0a.75.75 0 0 1 .75-.75h3.75a.75.75 0 0 1 0 1.5H9a.75.75 0 0 1-.75-.75ZM6 18a.75.75 0 0 1 .75-.75h.008a.75.75 0 0 1 .75.75v.008a.75.75 0 0 1-.75.75H6.75a.75.75 0 0 1-.75-.75V18Zm2.25 0a.75.75 0 0 1 .75-.75h3.75a.75.75 0 0 1 0 1.5H9a.75.75 0 0 1-.75-.75Z" clip-rule="evenodd" />
                            </svg>
                            Sign Up
                        </RouterLink>
                    </div>
                </template>
            </div>    
    </nav>

    <main class="px-8 py-6 bg-gray-100">
        <RouterView />
    </main>

    <div class="mt-10 footer-div flex items-center p-5 bg-[#410445] text-white justify-evenly">
        <div>
            <p class="text-2xl text-[#F6DC43]">FriendBuzz</p>
            <p class="text-md">All Rights reserved.</p>
        </div>

        <div class="footer-links text-md">
            <div><RouterLink to="/" active-class="active">Home</RouterLink></div>
            <div><RouterLink to="/login" active-class="active">Login</RouterLink></div>
            <div><RouterLink to="/signup" active-class="active">Signup</RouterLink></div>
        </div>

        <div>
            <p class="text-2xl">Contact Us</p>
            <p class="text-xl">ABC Street</p>
            <p class="text-xl">+91 0000000000</p>
        </div>

        <div class="footer-links2">
            <div><RouterLink to="/feed" active-class="active">Feed</RouterLink></div>
            <div><RouterLink to="/chat" active-class="active">Chat</RouterLink></div>
            <div><RouterLink to="/notifications" active-class="active">Notifications</RouterLink></div>
            <div><RouterLink to="/search" active-class="active">Search</RouterLink></div>
        </div>
    </div>

    <Toast />
</template>

<style>
nav{
    background-color: #410445;
    color: white;
}

.menu-left{
    color: #F6DC43;
    cursor: pointer;
}

.menu-right a{
    cursor: pointer;
}

.menu-center .active{
    color: #F6DC43;
    border-bottom: 5px solid #F6DC43;
}

.menu-right .active{
    color: #F6DC43;
    border-bottom: 5px solid #F6DC43;
}

.footer-links .active{
    color: #F6DC43;
}

.footer-links2 .active{
    color: #F6DC43;
}
</style>

<script>
    import axios from 'axios'
    import Toast from '@/components/Toast.vue'
    import { useUserStore } from '@/stores/user'

    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
        },

        components: {
            Toast
        },

        beforeCreate() {
            this.userStore.initStore()

            const token = this.userStore.user.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            } else {
                axios.defaults.headers.common["Authorization"] = "";
            }
        }
    }
</script>