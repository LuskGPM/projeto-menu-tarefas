from ..model.mysql_db import Categoria, CategoriaRepository

class CategoriaControler(CategoriaRepository):
    async def obter_categoria_por_id(self, categoria_id: int) -> dict:
        categoria: Categoria = await self._select_by_id(Categoria, categoria_id)
        return categoria.to_dict()
