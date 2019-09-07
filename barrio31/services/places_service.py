import logging
from barrio31.entities.place import Place


class PlacesService:

    @classmethod
    def get_all(cls):
        """ Obtener todos los lugares disponibles

        :return:
            lista de todos los lugares disponibles.
        """
        return [place.to_json() for place in Place.get()]

    @classmethod
    def get_place(cls, place_id):
        """ Obtener lugar especifico a partir de identificador

        :param place_id:
            identificador del lugar que se quiere buscar.
        :return:
            informacion del lugar con el id recibido por parametro.
        """

        return Place.get(place_id)

    @classmethod
    def create_place(cls, place_attributes):
        """ Crear nuevo lugar de interes con los atributos del lugar

        :param place_attributes:
            atributos/caracteristicas del lugar que se quiere crear.
        :return:
            informacion del lugar creado.
        """
        try:
            logging.info("Create place {}".format(place_attributes))
            place = Place(**place_attributes)
            place.save()
            return place
        except Exception as e:
            logging.error(e)

    @classmethod
    def delete_place(self, place_id):
        """
        :param place_id:
            identificador del lugar que se quiere eliminar.
        """
        place = Place.get(place_id)
        place.delete()
