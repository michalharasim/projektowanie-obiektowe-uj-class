<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\ORM\EntityManagerInterface;
use App\Entity\Product;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

#[Route('/product')]
final class ProductController extends AbstractController {

    #[Route('', name: 'product_all', methods: ['GET'])]    
    public function getAll(EntityManagerInterface $em): JsonResponse
    {
        $products = $em->getRepository(Product::class)->findAll();

        $data = array_map(fn($p) => [
            'id' => $p->getId(),
            'name' => $p->getName(),
            'price' => $p->getPrice()
        ], $products);

        return $this->json($data);
    }

    #[Route('', name: 'product_create', methods: ['POST'])]    
    public function create(Request $request, EntityManagerInterface $em): JsonResponse
    {
        $data = json_decode($request->getContent(), true);
        $product = new Product();
        $product->setName($data['name']);
        $product->setPrice($data['price']);

        $em->persist($product);
        $em->flush();

        return $this->json(['status' => 'created', 'id' => $product->getId()]);
    }

    #[Route('/{id}', name: 'product_find', methods: ['GET'])]    
    public function findById(Product $product): JsonResponse
    {
        return $this->json([
            'id' => $product->getId(),
            'name' => $product->getName(),
            'price' => $product->getPrice()
        ]);
    }

    #[Route('/{id}', name: 'product_update', methods: ['PUT'])]    
    public function update(Request $request, Product $product, EntityManagerInterface $em): JsonResponse
    {
        $data = json_decode($request->getContent(), true);

        $product->setName($data['name']);
        $product->setPrice($data['price']);

        $em->flush();

        return $this->json([
            'id' => $product->getId(),
            'name' => $product->getName(),
            'price' => $product->getPrice()
        ]);    
    }

    #[Route('/{id}', name: 'product_delete', methods: ['DeLEtE'])]    
    public function delete(Product $product, EntityManagerInterface $em): JsonResponse
    {
        $em->remove($product);
        $em->flush();

        return $this->json(['status' => 'deleted']);
    }
}
