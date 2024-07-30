def generate_openapi_spec():
    spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "API Autentikasi Pengguna",
            "version": "1.0.0",
            "description": "API untuk registrasi, login, dan akses resource yang dilindungi."
        },
        "paths": {
            "/api/register": {
                "post": {
                    "summary": "Registrasi pengguna baru",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {
                                            "type": "string",
                                            "description": "Nama pengguna"
                                        },
                                        "password": {
                                            "type": "string",
                                            "description": "Kata sandi"
                                        },
                                        "email": {
                                            "type": "string",
                                            "description": "Surel"
                                        }
                                    },
                                    "required": ["username", "password", "email"]
                                }
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Pengguna berhasil terdaftar"
                        },
                        "400": {
                            "description": "Permintaan tidak valid"
                        }
                    }
                }
            },
            "/api/login": {
                "post": {
                    "summary": "Login pengguna",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {
                                            "type": "string",
                                            "description": "Nama pengguna"
                                        },
                                        "password": {
                                            "type": "string",
                                            "description": "Kata sandi"
                                        }
                                    },
                                    "required": ["username", "password"]
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Login berhasil"
                        },
                        "401": {
                            "description": "Password salah"
                        }
                    }
                }
            },
            "/api/protected": {
                "get": {
                    "summary": "Akses resource yang dilindungi",
                    "security": [{
                        "bearerAuth": []
                    }],
                    "responses": {
                        "200": {
                            "description": "Akses berhasil"
                        },
                        "401": {
                            "description": "Tidak terautentikasi"
                        }
                    }
                }
            }
        },
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        }
    }
    return spec
