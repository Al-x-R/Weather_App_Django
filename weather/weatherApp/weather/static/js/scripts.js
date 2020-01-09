// Определяем переменную map
                        let map;

                        // Функция initMap которая отрисует карту на странице
                        function initMap() {

                            // В переменной map создаем объект карты GoogleMaps и вешаем эту переменную на <div id="map"></div>
                            map = new google.maps.Map(document.getElementById('map'), {
                                // При создании объекта карты необходимо указать его свойства
                                // center - определяем точку на которой карта будет центрироваться
                                center: {
                                    lat: 47.85,
                                    lng: 35.12
                                },
                                // zoom - определяет масштаб. 0 - видно всю платнеу. 18 - видно дома и улицы города.
                                zoom: 10,

                            });
                            // Создаем маркер на карте
                            let marker = new google.maps.Marker({

                                // Определяем позицию маркера
                                position: {
                                    lat: 47.85,
                                    lng: 35.12
                                },

                                // Указываем на какой карте он должен появится. (На странице ведь может быть больше одной карты)
                                map: map,
                            });
                            let coord;
                            google.maps.event.addListener(map, 'click', function (event) {
                                coord = event.latLng; // in event.latLng  you have the coordinates of click
                                alert(coord);
                            });
                        }