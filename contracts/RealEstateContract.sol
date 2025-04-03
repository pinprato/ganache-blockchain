// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RealEstateMarketplace {

    struct Property {
        uint256 id;
        address payable owner;
        string description;
        uint256 price;
        bool isForSale;
    }

    uint256 public propertyCount = 0;
    mapping(uint256 => Property) public properties;

    // Evento per la registrazione delle proprietà
    event PropertyRegistered(uint256 id, address owner, string description, uint256 price);

    // Evento per la vendita delle proprietà
    event PropertySold(uint256 id, address newOwner, uint256 price);

    // Registrazione di una nuova proprietà
    function registerProperty(string memory _description, uint256 _price) public {
        propertyCount++;
        properties[propertyCount] = Property(propertyCount, payable(msg.sender), _description, _price, true);
        emit PropertyRegistered(propertyCount, msg.sender, _description, _price);
    }

    // Acquisto di una proprietà
    function buyProperty(uint256 _id) public payable {
        Property storage property = properties[_id];
        require(property.isForSale, "La proprieta non e in vendita");
        require(msg.value >= property.price, "Importo insufficiente");

        // Pagamento al proprietario
        property.owner.transfer(property.price);
        
        // Cambio di proprietà
        property.owner = payable(msg.sender);
        property.isForSale = false;

        emit PropertySold(_id, msg.sender, property.price);
    }

    // Visualizzazione di tutte le proprietà disponibili
    function getProperties() public view returns (Property[] memory) {
        Property[] memory availableProperties = new Property[](propertyCount);
        uint256 counter = 0;
        for (uint256 i = 1; i <= propertyCount; i++) {
            if (properties[i].isForSale) {
                availableProperties[counter] = properties[i];
                counter++;
            }
        }
        return availableProperties;
    }
}
